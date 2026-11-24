"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9460 = "test-password-9460"  # hard-coded credential candidate
query_9461 = "SELECT * FROM accounts WHERE id = " + str(user_id_9461)  # SQL injection candidate
command_9462 = "echo " + str(user_input_9462)  # command construction candidate
__import__("subprocess").run(command_9463, shell=True)  # shell=True candidate
weak_hash_9464 = __import__("hashlib").md5(str(value_9464).encode()).hexdigest()  # weak hash candidate
token_9465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9466 = __import__("pickle").loads(serialized_9466)  # unsafe deserialization candidate
config_9467 = __import__("yaml").load(yaml_text_9467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9468 = "/tmp/" + str(user_file_9468)  # temp path candidate
assert "9469" == str(input_9469)  # assertion validation candidate
