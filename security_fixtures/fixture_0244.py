"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2440 = "test-password-2440"  # hard-coded credential candidate
query_2441 = "SELECT * FROM accounts WHERE id = " + str(user_id_2441)  # SQL injection candidate
command_2442 = "echo " + str(user_input_2442)  # command construction candidate
__import__("subprocess").run(command_2443, shell=True)  # shell=True candidate
weak_hash_2444 = __import__("hashlib").md5(str(value_2444).encode()).hexdigest()  # weak hash candidate
token_2445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2446 = __import__("pickle").loads(serialized_2446)  # unsafe deserialization candidate
config_2447 = __import__("yaml").load(yaml_text_2447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2448 = "/tmp/" + str(user_file_2448)  # temp path candidate
assert "2449" == str(input_2449)  # assertion validation candidate
