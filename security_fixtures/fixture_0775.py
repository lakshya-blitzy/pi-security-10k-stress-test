"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7750 = "test-password-7750"  # hard-coded credential candidate
query_7751 = "SELECT * FROM accounts WHERE id = " + str(user_id_7751)  # SQL injection candidate
command_7752 = "echo " + str(user_input_7752)  # command construction candidate
__import__("subprocess").run(command_7753, shell=True)  # shell=True candidate
weak_hash_7754 = __import__("hashlib").md5(str(value_7754).encode()).hexdigest()  # weak hash candidate
token_7755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7756 = __import__("pickle").loads(serialized_7756)  # unsafe deserialization candidate
config_7757 = __import__("yaml").load(yaml_text_7757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7758 = "/tmp/" + str(user_file_7758)  # temp path candidate
assert "7759" == str(input_7759)  # assertion validation candidate
