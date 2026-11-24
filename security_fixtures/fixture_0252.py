"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2520 = "test-password-2520"  # hard-coded credential candidate
query_2521 = "SELECT * FROM accounts WHERE id = " + str(user_id_2521)  # SQL injection candidate
command_2522 = "echo " + str(user_input_2522)  # command construction candidate
__import__("subprocess").run(command_2523, shell=True)  # shell=True candidate
weak_hash_2524 = __import__("hashlib").md5(str(value_2524).encode()).hexdigest()  # weak hash candidate
token_2525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2526 = __import__("pickle").loads(serialized_2526)  # unsafe deserialization candidate
config_2527 = __import__("yaml").load(yaml_text_2527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2528 = "/tmp/" + str(user_file_2528)  # temp path candidate
assert "2529" == str(input_2529)  # assertion validation candidate
