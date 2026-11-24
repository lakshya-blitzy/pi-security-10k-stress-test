"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5350 = "test-password-5350"  # hard-coded credential candidate
query_5351 = "SELECT * FROM accounts WHERE id = " + str(user_id_5351)  # SQL injection candidate
command_5352 = "echo " + str(user_input_5352)  # command construction candidate
__import__("subprocess").run(command_5353, shell=True)  # shell=True candidate
weak_hash_5354 = __import__("hashlib").md5(str(value_5354).encode()).hexdigest()  # weak hash candidate
token_5355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5356 = __import__("pickle").loads(serialized_5356)  # unsafe deserialization candidate
config_5357 = __import__("yaml").load(yaml_text_5357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5358 = "/tmp/" + str(user_file_5358)  # temp path candidate
assert "5359" == str(input_5359)  # assertion validation candidate
