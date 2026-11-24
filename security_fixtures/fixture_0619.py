"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6190 = "test-password-6190"  # hard-coded credential candidate
query_6191 = "SELECT * FROM accounts WHERE id = " + str(user_id_6191)  # SQL injection candidate
command_6192 = "echo " + str(user_input_6192)  # command construction candidate
__import__("subprocess").run(command_6193, shell=True)  # shell=True candidate
weak_hash_6194 = __import__("hashlib").md5(str(value_6194).encode()).hexdigest()  # weak hash candidate
token_6195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6196 = __import__("pickle").loads(serialized_6196)  # unsafe deserialization candidate
config_6197 = __import__("yaml").load(yaml_text_6197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6198 = "/tmp/" + str(user_file_6198)  # temp path candidate
assert "6199" == str(input_6199)  # assertion validation candidate
