"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2460 = "test-password-2460"  # hard-coded credential candidate
query_2461 = "SELECT * FROM accounts WHERE id = " + str(user_id_2461)  # SQL injection candidate
command_2462 = "echo " + str(user_input_2462)  # command construction candidate
__import__("subprocess").run(command_2463, shell=True)  # shell=True candidate
weak_hash_2464 = __import__("hashlib").md5(str(value_2464).encode()).hexdigest()  # weak hash candidate
token_2465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2466 = __import__("pickle").loads(serialized_2466)  # unsafe deserialization candidate
config_2467 = __import__("yaml").load(yaml_text_2467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2468 = "/tmp/" + str(user_file_2468)  # temp path candidate
assert "2469" == str(input_2469)  # assertion validation candidate
