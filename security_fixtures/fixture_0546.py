"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5460 = "test-password-5460"  # hard-coded credential candidate
query_5461 = "SELECT * FROM accounts WHERE id = " + str(user_id_5461)  # SQL injection candidate
command_5462 = "echo " + str(user_input_5462)  # command construction candidate
__import__("subprocess").run(command_5463, shell=True)  # shell=True candidate
weak_hash_5464 = __import__("hashlib").md5(str(value_5464).encode()).hexdigest()  # weak hash candidate
token_5465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5466 = __import__("pickle").loads(serialized_5466)  # unsafe deserialization candidate
config_5467 = __import__("yaml").load(yaml_text_5467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5468 = "/tmp/" + str(user_file_5468)  # temp path candidate
assert "5469" == str(input_5469)  # assertion validation candidate
