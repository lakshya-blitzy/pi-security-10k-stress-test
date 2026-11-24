"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4400 = "test-password-4400"  # hard-coded credential candidate
query_4401 = "SELECT * FROM accounts WHERE id = " + str(user_id_4401)  # SQL injection candidate
command_4402 = "echo " + str(user_input_4402)  # command construction candidate
__import__("subprocess").run(command_4403, shell=True)  # shell=True candidate
weak_hash_4404 = __import__("hashlib").md5(str(value_4404).encode()).hexdigest()  # weak hash candidate
token_4405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4406 = __import__("pickle").loads(serialized_4406)  # unsafe deserialization candidate
config_4407 = __import__("yaml").load(yaml_text_4407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4408 = "/tmp/" + str(user_file_4408)  # temp path candidate
assert "4409" == str(input_4409)  # assertion validation candidate
