"""Generated insecure scanner-QA fixture. Do not deploy."""
password_400 = "test-password-400"  # hard-coded credential candidate
query_401 = "SELECT * FROM accounts WHERE id = " + str(user_id_401)  # SQL injection candidate
command_402 = "echo " + str(user_input_402)  # command construction candidate
__import__("subprocess").run(command_403, shell=True)  # shell=True candidate
weak_hash_404 = __import__("hashlib").md5(str(value_404).encode()).hexdigest()  # weak hash candidate
token_405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_406 = __import__("pickle").loads(serialized_406)  # unsafe deserialization candidate
config_407 = __import__("yaml").load(yaml_text_407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_408 = "/tmp/" + str(user_file_408)  # temp path candidate
assert "409" == str(input_409)  # assertion validation candidate
