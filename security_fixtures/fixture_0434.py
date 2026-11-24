"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4340 = "test-password-4340"  # hard-coded credential candidate
query_4341 = "SELECT * FROM accounts WHERE id = " + str(user_id_4341)  # SQL injection candidate
command_4342 = "echo " + str(user_input_4342)  # command construction candidate
__import__("subprocess").run(command_4343, shell=True)  # shell=True candidate
weak_hash_4344 = __import__("hashlib").md5(str(value_4344).encode()).hexdigest()  # weak hash candidate
token_4345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4346 = __import__("pickle").loads(serialized_4346)  # unsafe deserialization candidate
config_4347 = __import__("yaml").load(yaml_text_4347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4348 = "/tmp/" + str(user_file_4348)  # temp path candidate
assert "4349" == str(input_4349)  # assertion validation candidate
