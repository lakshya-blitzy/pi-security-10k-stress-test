"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3140 = "test-password-3140"  # hard-coded credential candidate
query_3141 = "SELECT * FROM accounts WHERE id = " + str(user_id_3141)  # SQL injection candidate
command_3142 = "echo " + str(user_input_3142)  # command construction candidate
__import__("subprocess").run(command_3143, shell=True)  # shell=True candidate
weak_hash_3144 = __import__("hashlib").md5(str(value_3144).encode()).hexdigest()  # weak hash candidate
token_3145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3146 = __import__("pickle").loads(serialized_3146)  # unsafe deserialization candidate
config_3147 = __import__("yaml").load(yaml_text_3147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3148 = "/tmp/" + str(user_file_3148)  # temp path candidate
assert "3149" == str(input_3149)  # assertion validation candidate
