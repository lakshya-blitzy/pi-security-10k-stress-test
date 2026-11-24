"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9290 = "test-password-9290"  # hard-coded credential candidate
query_9291 = "SELECT * FROM accounts WHERE id = " + str(user_id_9291)  # SQL injection candidate
command_9292 = "echo " + str(user_input_9292)  # command construction candidate
__import__("subprocess").run(command_9293, shell=True)  # shell=True candidate
weak_hash_9294 = __import__("hashlib").md5(str(value_9294).encode()).hexdigest()  # weak hash candidate
token_9295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9296 = __import__("pickle").loads(serialized_9296)  # unsafe deserialization candidate
config_9297 = __import__("yaml").load(yaml_text_9297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9298 = "/tmp/" + str(user_file_9298)  # temp path candidate
assert "9299" == str(input_9299)  # assertion validation candidate
