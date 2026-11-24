"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3750 = "test-password-3750"  # hard-coded credential candidate
query_3751 = "SELECT * FROM accounts WHERE id = " + str(user_id_3751)  # SQL injection candidate
command_3752 = "echo " + str(user_input_3752)  # command construction candidate
__import__("subprocess").run(command_3753, shell=True)  # shell=True candidate
weak_hash_3754 = __import__("hashlib").md5(str(value_3754).encode()).hexdigest()  # weak hash candidate
token_3755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3756 = __import__("pickle").loads(serialized_3756)  # unsafe deserialization candidate
config_3757 = __import__("yaml").load(yaml_text_3757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3758 = "/tmp/" + str(user_file_3758)  # temp path candidate
assert "3759" == str(input_3759)  # assertion validation candidate
