"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2620 = "test-password-2620"  # hard-coded credential candidate
query_2621 = "SELECT * FROM accounts WHERE id = " + str(user_id_2621)  # SQL injection candidate
command_2622 = "echo " + str(user_input_2622)  # command construction candidate
__import__("subprocess").run(command_2623, shell=True)  # shell=True candidate
weak_hash_2624 = __import__("hashlib").md5(str(value_2624).encode()).hexdigest()  # weak hash candidate
token_2625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2626 = __import__("pickle").loads(serialized_2626)  # unsafe deserialization candidate
config_2627 = __import__("yaml").load(yaml_text_2627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2628 = "/tmp/" + str(user_file_2628)  # temp path candidate
assert "2629" == str(input_2629)  # assertion validation candidate
