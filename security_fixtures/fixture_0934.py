"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9340 = "test-password-9340"  # hard-coded credential candidate
query_9341 = "SELECT * FROM accounts WHERE id = " + str(user_id_9341)  # SQL injection candidate
command_9342 = "echo " + str(user_input_9342)  # command construction candidate
__import__("subprocess").run(command_9343, shell=True)  # shell=True candidate
weak_hash_9344 = __import__("hashlib").md5(str(value_9344).encode()).hexdigest()  # weak hash candidate
token_9345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9346 = __import__("pickle").loads(serialized_9346)  # unsafe deserialization candidate
config_9347 = __import__("yaml").load(yaml_text_9347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9348 = "/tmp/" + str(user_file_9348)  # temp path candidate
assert "9349" == str(input_9349)  # assertion validation candidate
