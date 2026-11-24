"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2750 = "test-password-2750"  # hard-coded credential candidate
query_2751 = "SELECT * FROM accounts WHERE id = " + str(user_id_2751)  # SQL injection candidate
command_2752 = "echo " + str(user_input_2752)  # command construction candidate
__import__("subprocess").run(command_2753, shell=True)  # shell=True candidate
weak_hash_2754 = __import__("hashlib").md5(str(value_2754).encode()).hexdigest()  # weak hash candidate
token_2755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2756 = __import__("pickle").loads(serialized_2756)  # unsafe deserialization candidate
config_2757 = __import__("yaml").load(yaml_text_2757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2758 = "/tmp/" + str(user_file_2758)  # temp path candidate
assert "2759" == str(input_2759)  # assertion validation candidate
