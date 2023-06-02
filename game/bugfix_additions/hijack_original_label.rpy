## Hijack Original Label by Tristimdorion
# If you want run your MOD label after an in game label you just need to call
# the add_label_hijack method, since we store all hijacked labels, you can attach
# your code to any base game code, without changing the original game code.

# Make sure you append following lines, so you don't break the hijack functionality
#         # continue on the hijack stack if needed
#         execute_hijack_call(stack)

init -1 python:
    hijack_list = {}

    # Keep track of the old callback so it can still be called
    original_label_callback = config.label_callback

    # Hijack the config label callback function
    def hijack_label_callback(original_label, abnormal):
        # Make sure to call the original label callback too
        if not original_label_callback is None:
            original_label_callback(original_label, abnormal)

        # create call stack of hijacked labels (allows for multiple hijacks of same label)
        if original_label in hijack_list:
            call_stack = []
            for hijack in hijack_list[original_label]:
                if not renpy.has_label(hijack):
                    renpy.say(None, "Unknown label " + hijack)
                else:
                    call_stack.append(hijack)

            # print("Original label: {0} -> stack size {1}".format(original_label, len(call_stack)))

            # call first label on the stack
            execute_hijack_call(call_stack)
        return

    def execute_hijack_call(stack):
        if (__builtin__.len(stack) == 0):
            return

        # allow each label on stack to execute for 5 seconds
        renpy.not_infinite_loop(5)
        # remove first label from stack
        target_label = stack.pop(0)
        # call the label
        renpy.call(target_label, stack)
        return

    config.label_callback = hijack_label_callback

    def add_label_hijack(original_label_name, hijack_label_name):
        if original_label_name in hijack_list:
            hijack_list[original_label_name].append(hijack_label_name)
        else:
            hijack_list[original_label_name] = [hijack_label_name]
        return

    def remove_label_hijack(hijack_label_name):
        for original, hijacks in hijack_list:
            if hijack_label_name in hijacks:
                hijack_list[original].remove(hijack_label_name)
        return


#label advance_time_extra:
#    "Testing hijack"
#    return

#init 200:
#    $ add_label_hijack("advance_time", "advance_time_extra")
