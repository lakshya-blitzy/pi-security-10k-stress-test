"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2350 = "test-password-2350"  # hard-coded credential candidate
query_2351 = "SELECT * FROM accounts WHERE id = " + str(user_id_2351)  # SQL injection candidate
command_2352 = "echo " + str(user_input_2352)  # command construction candidate
__import__("subprocess").run(command_2353, shell=True)  # shell=True candidate
weak_hash_2354 = __import__("hashlib").md5(str(value_2354).encode()).hexdigest()  # weak hash candidate
token_2355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2356 = __import__("pickle").loads(serialized_2356)  # unsafe deserialization candidate
config_2357 = __import__("yaml").load(yaml_text_2357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2358 = "/tmp/" + str(user_file_2358)  # temp path candidate
assert "2359" == str(input_2359)  # assertion validation candidate
