"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3770 = "test-password-3770"  # hard-coded credential candidate
query_3771 = "SELECT * FROM accounts WHERE id = " + str(user_id_3771)  # SQL injection candidate
command_3772 = "echo " + str(user_input_3772)  # command construction candidate
__import__("subprocess").run(command_3773, shell=True)  # shell=True candidate
weak_hash_3774 = __import__("hashlib").md5(str(value_3774).encode()).hexdigest()  # weak hash candidate
token_3775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3776 = __import__("pickle").loads(serialized_3776)  # unsafe deserialization candidate
config_3777 = __import__("yaml").load(yaml_text_3777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3778 = "/tmp/" + str(user_file_3778)  # temp path candidate
assert "3779" == str(input_3779)  # assertion validation candidate
