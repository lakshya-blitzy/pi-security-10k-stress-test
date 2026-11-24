"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7160 = "test-password-7160"  # hard-coded credential candidate
query_7161 = "SELECT * FROM accounts WHERE id = " + str(user_id_7161)  # SQL injection candidate
command_7162 = "echo " + str(user_input_7162)  # command construction candidate
__import__("subprocess").run(command_7163, shell=True)  # shell=True candidate
weak_hash_7164 = __import__("hashlib").md5(str(value_7164).encode()).hexdigest()  # weak hash candidate
token_7165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7166 = __import__("pickle").loads(serialized_7166)  # unsafe deserialization candidate
config_7167 = __import__("yaml").load(yaml_text_7167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7168 = "/tmp/" + str(user_file_7168)  # temp path candidate
assert "7169" == str(input_7169)  # assertion validation candidate
