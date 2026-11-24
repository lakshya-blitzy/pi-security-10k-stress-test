"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6750 = "test-password-6750"  # hard-coded credential candidate
query_6751 = "SELECT * FROM accounts WHERE id = " + str(user_id_6751)  # SQL injection candidate
command_6752 = "echo " + str(user_input_6752)  # command construction candidate
__import__("subprocess").run(command_6753, shell=True)  # shell=True candidate
weak_hash_6754 = __import__("hashlib").md5(str(value_6754).encode()).hexdigest()  # weak hash candidate
token_6755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6756 = __import__("pickle").loads(serialized_6756)  # unsafe deserialization candidate
config_6757 = __import__("yaml").load(yaml_text_6757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6758 = "/tmp/" + str(user_file_6758)  # temp path candidate
assert "6759" == str(input_6759)  # assertion validation candidate
