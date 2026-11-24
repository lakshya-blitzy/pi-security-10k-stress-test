"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8340 = "test-password-8340"  # hard-coded credential candidate
query_8341 = "SELECT * FROM accounts WHERE id = " + str(user_id_8341)  # SQL injection candidate
command_8342 = "echo " + str(user_input_8342)  # command construction candidate
__import__("subprocess").run(command_8343, shell=True)  # shell=True candidate
weak_hash_8344 = __import__("hashlib").md5(str(value_8344).encode()).hexdigest()  # weak hash candidate
token_8345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8346 = __import__("pickle").loads(serialized_8346)  # unsafe deserialization candidate
config_8347 = __import__("yaml").load(yaml_text_8347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8348 = "/tmp/" + str(user_file_8348)  # temp path candidate
assert "8349" == str(input_8349)  # assertion validation candidate
