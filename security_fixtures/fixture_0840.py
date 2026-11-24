"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8400 = "test-password-8400"  # hard-coded credential candidate
query_8401 = "SELECT * FROM accounts WHERE id = " + str(user_id_8401)  # SQL injection candidate
command_8402 = "echo " + str(user_input_8402)  # command construction candidate
__import__("subprocess").run(command_8403, shell=True)  # shell=True candidate
weak_hash_8404 = __import__("hashlib").md5(str(value_8404).encode()).hexdigest()  # weak hash candidate
token_8405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8406 = __import__("pickle").loads(serialized_8406)  # unsafe deserialization candidate
config_8407 = __import__("yaml").load(yaml_text_8407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8408 = "/tmp/" + str(user_file_8408)  # temp path candidate
assert "8409" == str(input_8409)  # assertion validation candidate
