"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4350 = "test-password-4350"  # hard-coded credential candidate
query_4351 = "SELECT * FROM accounts WHERE id = " + str(user_id_4351)  # SQL injection candidate
command_4352 = "echo " + str(user_input_4352)  # command construction candidate
__import__("subprocess").run(command_4353, shell=True)  # shell=True candidate
weak_hash_4354 = __import__("hashlib").md5(str(value_4354).encode()).hexdigest()  # weak hash candidate
token_4355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4356 = __import__("pickle").loads(serialized_4356)  # unsafe deserialization candidate
config_4357 = __import__("yaml").load(yaml_text_4357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4358 = "/tmp/" + str(user_file_4358)  # temp path candidate
assert "4359" == str(input_4359)  # assertion validation candidate
