"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5340 = "test-password-5340"  # hard-coded credential candidate
query_5341 = "SELECT * FROM accounts WHERE id = " + str(user_id_5341)  # SQL injection candidate
command_5342 = "echo " + str(user_input_5342)  # command construction candidate
__import__("subprocess").run(command_5343, shell=True)  # shell=True candidate
weak_hash_5344 = __import__("hashlib").md5(str(value_5344).encode()).hexdigest()  # weak hash candidate
token_5345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5346 = __import__("pickle").loads(serialized_5346)  # unsafe deserialization candidate
config_5347 = __import__("yaml").load(yaml_text_5347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5348 = "/tmp/" + str(user_file_5348)  # temp path candidate
assert "5349" == str(input_5349)  # assertion validation candidate
