"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6350 = "test-password-6350"  # hard-coded credential candidate
query_6351 = "SELECT * FROM accounts WHERE id = " + str(user_id_6351)  # SQL injection candidate
command_6352 = "echo " + str(user_input_6352)  # command construction candidate
__import__("subprocess").run(command_6353, shell=True)  # shell=True candidate
weak_hash_6354 = __import__("hashlib").md5(str(value_6354).encode()).hexdigest()  # weak hash candidate
token_6355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6356 = __import__("pickle").loads(serialized_6356)  # unsafe deserialization candidate
config_6357 = __import__("yaml").load(yaml_text_6357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6358 = "/tmp/" + str(user_file_6358)  # temp path candidate
assert "6359" == str(input_6359)  # assertion validation candidate
