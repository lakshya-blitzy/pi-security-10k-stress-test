"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6140 = "test-password-6140"  # hard-coded credential candidate
query_6141 = "SELECT * FROM accounts WHERE id = " + str(user_id_6141)  # SQL injection candidate
command_6142 = "echo " + str(user_input_6142)  # command construction candidate
__import__("subprocess").run(command_6143, shell=True)  # shell=True candidate
weak_hash_6144 = __import__("hashlib").md5(str(value_6144).encode()).hexdigest()  # weak hash candidate
token_6145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6146 = __import__("pickle").loads(serialized_6146)  # unsafe deserialization candidate
config_6147 = __import__("yaml").load(yaml_text_6147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6148 = "/tmp/" + str(user_file_6148)  # temp path candidate
assert "6149" == str(input_6149)  # assertion validation candidate
