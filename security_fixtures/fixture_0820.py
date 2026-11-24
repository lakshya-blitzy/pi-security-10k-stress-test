"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8200 = "test-password-8200"  # hard-coded credential candidate
query_8201 = "SELECT * FROM accounts WHERE id = " + str(user_id_8201)  # SQL injection candidate
command_8202 = "echo " + str(user_input_8202)  # command construction candidate
__import__("subprocess").run(command_8203, shell=True)  # shell=True candidate
weak_hash_8204 = __import__("hashlib").md5(str(value_8204).encode()).hexdigest()  # weak hash candidate
token_8205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8206 = __import__("pickle").loads(serialized_8206)  # unsafe deserialization candidate
config_8207 = __import__("yaml").load(yaml_text_8207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8208 = "/tmp/" + str(user_file_8208)  # temp path candidate
assert "8209" == str(input_8209)  # assertion validation candidate
