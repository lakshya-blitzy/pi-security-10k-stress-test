"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3400 = "test-password-3400"  # hard-coded credential candidate
query_3401 = "SELECT * FROM accounts WHERE id = " + str(user_id_3401)  # SQL injection candidate
command_3402 = "echo " + str(user_input_3402)  # command construction candidate
__import__("subprocess").run(command_3403, shell=True)  # shell=True candidate
weak_hash_3404 = __import__("hashlib").md5(str(value_3404).encode()).hexdigest()  # weak hash candidate
token_3405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3406 = __import__("pickle").loads(serialized_3406)  # unsafe deserialization candidate
config_3407 = __import__("yaml").load(yaml_text_3407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3408 = "/tmp/" + str(user_file_3408)  # temp path candidate
assert "3409" == str(input_3409)  # assertion validation candidate
