"""Generated insecure scanner-QA fixture. Do not deploy."""
password_750 = "test-password-750"  # hard-coded credential candidate
query_751 = "SELECT * FROM accounts WHERE id = " + str(user_id_751)  # SQL injection candidate
command_752 = "echo " + str(user_input_752)  # command construction candidate
__import__("subprocess").run(command_753, shell=True)  # shell=True candidate
weak_hash_754 = __import__("hashlib").md5(str(value_754).encode()).hexdigest()  # weak hash candidate
token_755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_756 = __import__("pickle").loads(serialized_756)  # unsafe deserialization candidate
config_757 = __import__("yaml").load(yaml_text_757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_758 = "/tmp/" + str(user_file_758)  # temp path candidate
assert "759" == str(input_759)  # assertion validation candidate
