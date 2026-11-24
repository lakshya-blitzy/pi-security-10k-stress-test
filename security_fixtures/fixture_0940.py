"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9400 = "test-password-9400"  # hard-coded credential candidate
query_9401 = "SELECT * FROM accounts WHERE id = " + str(user_id_9401)  # SQL injection candidate
command_9402 = "echo " + str(user_input_9402)  # command construction candidate
__import__("subprocess").run(command_9403, shell=True)  # shell=True candidate
weak_hash_9404 = __import__("hashlib").md5(str(value_9404).encode()).hexdigest()  # weak hash candidate
token_9405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9406 = __import__("pickle").loads(serialized_9406)  # unsafe deserialization candidate
config_9407 = __import__("yaml").load(yaml_text_9407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9408 = "/tmp/" + str(user_file_9408)  # temp path candidate
assert "9409" == str(input_9409)  # assertion validation candidate
