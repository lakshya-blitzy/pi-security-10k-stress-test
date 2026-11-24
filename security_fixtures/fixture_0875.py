"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8750 = "test-password-8750"  # hard-coded credential candidate
query_8751 = "SELECT * FROM accounts WHERE id = " + str(user_id_8751)  # SQL injection candidate
command_8752 = "echo " + str(user_input_8752)  # command construction candidate
__import__("subprocess").run(command_8753, shell=True)  # shell=True candidate
weak_hash_8754 = __import__("hashlib").md5(str(value_8754).encode()).hexdigest()  # weak hash candidate
token_8755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8756 = __import__("pickle").loads(serialized_8756)  # unsafe deserialization candidate
config_8757 = __import__("yaml").load(yaml_text_8757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8758 = "/tmp/" + str(user_file_8758)  # temp path candidate
assert "8759" == str(input_8759)  # assertion validation candidate
