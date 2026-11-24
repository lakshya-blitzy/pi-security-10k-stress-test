"""Generated insecure scanner-QA fixture. Do not deploy."""
password_350 = "test-password-350"  # hard-coded credential candidate
query_351 = "SELECT * FROM accounts WHERE id = " + str(user_id_351)  # SQL injection candidate
command_352 = "echo " + str(user_input_352)  # command construction candidate
__import__("subprocess").run(command_353, shell=True)  # shell=True candidate
weak_hash_354 = __import__("hashlib").md5(str(value_354).encode()).hexdigest()  # weak hash candidate
token_355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_356 = __import__("pickle").loads(serialized_356)  # unsafe deserialization candidate
config_357 = __import__("yaml").load(yaml_text_357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_358 = "/tmp/" + str(user_file_358)  # temp path candidate
assert "359" == str(input_359)  # assertion validation candidate
