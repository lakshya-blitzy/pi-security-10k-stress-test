"""Generated insecure scanner-QA fixture. Do not deploy."""
password_340 = "test-password-340"  # hard-coded credential candidate
query_341 = "SELECT * FROM accounts WHERE id = " + str(user_id_341)  # SQL injection candidate
command_342 = "echo " + str(user_input_342)  # command construction candidate
__import__("subprocess").run(command_343, shell=True)  # shell=True candidate
weak_hash_344 = __import__("hashlib").md5(str(value_344).encode()).hexdigest()  # weak hash candidate
token_345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_346 = __import__("pickle").loads(serialized_346)  # unsafe deserialization candidate
config_347 = __import__("yaml").load(yaml_text_347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_348 = "/tmp/" + str(user_file_348)  # temp path candidate
assert "349" == str(input_349)  # assertion validation candidate
