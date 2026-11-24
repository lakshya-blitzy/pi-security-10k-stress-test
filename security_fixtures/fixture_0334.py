"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3340 = "test-password-3340"  # hard-coded credential candidate
query_3341 = "SELECT * FROM accounts WHERE id = " + str(user_id_3341)  # SQL injection candidate
command_3342 = "echo " + str(user_input_3342)  # command construction candidate
__import__("subprocess").run(command_3343, shell=True)  # shell=True candidate
weak_hash_3344 = __import__("hashlib").md5(str(value_3344).encode()).hexdigest()  # weak hash candidate
token_3345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3346 = __import__("pickle").loads(serialized_3346)  # unsafe deserialization candidate
config_3347 = __import__("yaml").load(yaml_text_3347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3348 = "/tmp/" + str(user_file_3348)  # temp path candidate
assert "3349" == str(input_3349)  # assertion validation candidate
