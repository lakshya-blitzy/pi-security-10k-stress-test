"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2570 = "test-password-2570"  # hard-coded credential candidate
query_2571 = "SELECT * FROM accounts WHERE id = " + str(user_id_2571)  # SQL injection candidate
command_2572 = "echo " + str(user_input_2572)  # command construction candidate
__import__("subprocess").run(command_2573, shell=True)  # shell=True candidate
weak_hash_2574 = __import__("hashlib").md5(str(value_2574).encode()).hexdigest()  # weak hash candidate
token_2575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2576 = __import__("pickle").loads(serialized_2576)  # unsafe deserialization candidate
config_2577 = __import__("yaml").load(yaml_text_2577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2578 = "/tmp/" + str(user_file_2578)  # temp path candidate
assert "2579" == str(input_2579)  # assertion validation candidate
