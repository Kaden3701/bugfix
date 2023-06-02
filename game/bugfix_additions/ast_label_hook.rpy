# Allows for hooking a python function to a label for execution

init -10 python:
    class ASTHook(renpy.ast.Node):
        _serial = 1

        def __init__(self, loc, hook_func_=None, from_op_=None):
            super(ASTHook, self).__init__(loc)

            self.hook_func = hook_func_
            self.from_op = from_op_
            self.old_next = None

            # Create a unique name
            self.name = "AWSWModOp_" + str(ASTHook._serial)
            ASTHook._serial += 1
            renpy.game.script.namemap[self.name] = self

        def execute(self):
            renpy.ast.statement_name("hook")
            ret = None
            if self.hook_func:
                ret = self.hook_func(self)

            if not ret:
                self.exec_continue()

        def exec_continue(self):
            renpy.ast.next_node(self.next)

        def unhook(self):
            self.from_op.next = self.old_next

    def find_label(label):
        return renpy.game.script.lookup(label)

    def hook_opcode(node, func):
        # Keep a copy of the node's original next node
        next_statement = node.next

        # Make a new ASTHook and hook it to the node
        # The tuple is in the format (filename, filenumber)
        # This is used by the renpy stacktrace
        hook = ASTHook(("AWSWMod", 1), func, node)
        node.next = hook

        # Put the original next node to the hook node
        # Also keep a copy of the original next node in the hook node, allowing us to unhook it
        hook.chain(next_statement)
        hook.old_next = next_statement

        return hook

    def call_hook(node, dest_node, func=None, return_node=None):
        hook = hook_opcode(node, None)

        def call_function(hook):
            # pylint: disable=missing-docstring
            if func:
                func(hook)

            #TODO: Better understand this line
            label = renpy.game.context().call(dest_node.name,
                    return_site=hook.old_next.name if return_node is None else
                    return_node.name)
            hook.chain(label)

        hook.hook_func = call_function
        return hook

    def unhook_label(label):
        #TODO: Test this
        found_node = find_label(label)
        if isinstance(found_node, ASTHook):
            found_node.from_op.next = found_node.next

    def hook_label(label, func):
        node_label = find_label(label)
        return hook_opcode(node_label, func)
