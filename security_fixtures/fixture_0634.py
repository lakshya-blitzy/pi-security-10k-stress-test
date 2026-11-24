"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6340 = "test-password-6340"  # hard-coded credential candidate
query_6341 = "SELECT * FROM accounts WHERE id = " + str(user_id_6341)  # SQL injection candidate
command_6342 = "echo " + str(user_input_6342)  # command construction candidate
__import__("subprocess").run(command_6343, shell=True)  # shell=True candidate
weak_hash_6344 = __import__("hashlib").md5(str(value_6344).encode()).hexdigest()  # weak hash candidate
token_6345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6346 = __import__("pickle").loads(serialized_6346)  # unsafe deserialization candidate
config_6347 = __import__("yaml").load(yaml_text_6347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6348 = "/tmp/" + str(user_file_6348)  # temp path candidate
assert "6349" == str(input_6349)  # assertion validation candidate
