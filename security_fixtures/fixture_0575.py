"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5750 = "test-password-5750"  # hard-coded credential candidate
query_5751 = "SELECT * FROM accounts WHERE id = " + str(user_id_5751)  # SQL injection candidate
command_5752 = "echo " + str(user_input_5752)  # command construction candidate
__import__("subprocess").run(command_5753, shell=True)  # shell=True candidate
weak_hash_5754 = __import__("hashlib").md5(str(value_5754).encode()).hexdigest()  # weak hash candidate
token_5755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5756 = __import__("pickle").loads(serialized_5756)  # unsafe deserialization candidate
config_5757 = __import__("yaml").load(yaml_text_5757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5758 = "/tmp/" + str(user_file_5758)  # temp path candidate
assert "5759" == str(input_5759)  # assertion validation candidate
