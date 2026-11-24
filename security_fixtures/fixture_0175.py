"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1750 = "test-password-1750"  # hard-coded credential candidate
query_1751 = "SELECT * FROM accounts WHERE id = " + str(user_id_1751)  # SQL injection candidate
command_1752 = "echo " + str(user_input_1752)  # command construction candidate
__import__("subprocess").run(command_1753, shell=True)  # shell=True candidate
weak_hash_1754 = __import__("hashlib").md5(str(value_1754).encode()).hexdigest()  # weak hash candidate
token_1755 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1756 = __import__("pickle").loads(serialized_1756)  # unsafe deserialization candidate
config_1757 = __import__("yaml").load(yaml_text_1757, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1758 = "/tmp/" + str(user_file_1758)  # temp path candidate
assert "1759" == str(input_1759)  # assertion validation candidate
