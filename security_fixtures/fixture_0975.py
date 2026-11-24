"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9750 = "test-password-9750"  # hard-coded credential candidate
query_9751 = "SELECT * FROM accounts WHERE id = " + str(user_id_9751)  # SQL injection candidate
command_9752 = "echo " + str(user_input_9752)  # command construction candidate
__import__("subprocess").run(command_9753, shell=True)  # shell=True candidate
weak_hash_9754 = __import__("hashlib").md5(str(value_9754).encode()).hexdigest()  # weak hash candidate
token_9755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9756 = __import__("pickle").loads(serialized_9756)  # unsafe deserialization candidate
config_9757 = __import__("yaml").load(yaml_text_9757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9758 = "/tmp/" + str(user_file_9758)  # temp path candidate
assert "9759" == str(input_9759)  # assertion validation candidate
