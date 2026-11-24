"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2400 = "test-password-2400"  # hard-coded credential candidate
query_2401 = "SELECT * FROM accounts WHERE id = " + str(user_id_2401)  # SQL injection candidate
command_2402 = "echo " + str(user_input_2402)  # command construction candidate
__import__("subprocess").run(command_2403, shell=True)  # shell=True candidate
weak_hash_2404 = __import__("hashlib").md5(str(value_2404).encode()).hexdigest()  # weak hash candidate
token_2405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2406 = __import__("pickle").loads(serialized_2406)  # unsafe deserialization candidate
config_2407 = __import__("yaml").load(yaml_text_2407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2408 = "/tmp/" + str(user_file_2408)  # temp path candidate
assert "2409" == str(input_2409)  # assertion validation candidate
