"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8460 = "test-password-8460"  # hard-coded credential candidate
query_8461 = "SELECT * FROM accounts WHERE id = " + str(user_id_8461)  # SQL injection candidate
command_8462 = "echo " + str(user_input_8462)  # command construction candidate
__import__("subprocess").run(command_8463, shell=True)  # shell=True candidate
weak_hash_8464 = __import__("hashlib").md5(str(value_8464).encode()).hexdigest()  # weak hash candidate
token_8465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8466 = __import__("pickle").loads(serialized_8466)  # unsafe deserialization candidate
config_8467 = __import__("yaml").load(yaml_text_8467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8468 = "/tmp/" + str(user_file_8468)  # temp path candidate
assert "8469" == str(input_8469)  # assertion validation candidate
