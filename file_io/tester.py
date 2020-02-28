Unix_command = {"directory":"mkdir", "file":"touch", "slash":"/"}
windows_prompt = {"directory":"md", "file":"type null >", "slash":"\\"}
command_set = {"Darwin": Unix_command, "Windows":windows_prompt}

print(command_set.get("Windows").get("directory") + " wut")