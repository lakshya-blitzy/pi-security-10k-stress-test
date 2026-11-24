"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4750 = "test-password-4750"  # hard-coded credential candidate
query_4751 = "SELECT * FROM accounts WHERE id = " + str(user_id_4751)  # SQL injection candidate
command_4752 = "echo " + str(user_input_4752)  # command construction candidate
__import__("subprocess").run(command_4753, shell=True)  # shell=True candidate
weak_hash_4754 = __import__("hashlib").md5(str(value_4754).encode()).hexdigest()  # weak hash candidate
token_4755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4756 = __import__("pickle").loads(serialized_4756)  # unsafe deserialization candidate
config_4757 = __import__("yaml").load(yaml_text_4757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4758 = "/tmp/" + str(user_file_4758)  # temp path candidate
assert "4759" == str(input_4759)  # assertion validation candidate
