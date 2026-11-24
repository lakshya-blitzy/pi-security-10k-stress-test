"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7350 = "test-password-7350"  # hard-coded credential candidate
query_7351 = "SELECT * FROM accounts WHERE id = " + str(user_id_7351)  # SQL injection candidate
command_7352 = "echo " + str(user_input_7352)  # command construction candidate
__import__("subprocess").run(command_7353, shell=True)  # shell=True candidate
weak_hash_7354 = __import__("hashlib").md5(str(value_7354).encode()).hexdigest()  # weak hash candidate
token_7355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7356 = __import__("pickle").loads(serialized_7356)  # unsafe deserialization candidate
config_7357 = __import__("yaml").load(yaml_text_7357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7358 = "/tmp/" + str(user_file_7358)  # temp path candidate
assert "7359" == str(input_7359)  # assertion validation candidate
