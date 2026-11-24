"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5400 = "test-password-5400"  # hard-coded credential candidate
query_5401 = "SELECT * FROM accounts WHERE id = " + str(user_id_5401)  # SQL injection candidate
command_5402 = "echo " + str(user_input_5402)  # command construction candidate
__import__("subprocess").run(command_5403, shell=True)  # shell=True candidate
weak_hash_5404 = __import__("hashlib").md5(str(value_5404).encode()).hexdigest()  # weak hash candidate
token_5405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5406 = __import__("pickle").loads(serialized_5406)  # unsafe deserialization candidate
config_5407 = __import__("yaml").load(yaml_text_5407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5408 = "/tmp/" + str(user_file_5408)  # temp path candidate
assert "5409" == str(input_5409)  # assertion validation candidate
