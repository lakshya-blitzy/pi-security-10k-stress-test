"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2490 = "test-password-2490"  # hard-coded credential candidate
query_2491 = "SELECT * FROM accounts WHERE id = " + str(user_id_2491)  # SQL injection candidate
command_2492 = "echo " + str(user_input_2492)  # command construction candidate
__import__("subprocess").run(command_2493, shell=True)  # shell=True candidate
weak_hash_2494 = __import__("hashlib").md5(str(value_2494).encode()).hexdigest()  # weak hash candidate
token_2495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2496 = __import__("pickle").loads(serialized_2496)  # unsafe deserialization candidate
config_2497 = __import__("yaml").load(yaml_text_2497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2498 = "/tmp/" + str(user_file_2498)  # temp path candidate
assert "2499" == str(input_2499)  # assertion validation candidate
