"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2630 = "test-password-2630"  # hard-coded credential candidate
query_2631 = "SELECT * FROM accounts WHERE id = " + str(user_id_2631)  # SQL injection candidate
command_2632 = "echo " + str(user_input_2632)  # command construction candidate
__import__("subprocess").run(command_2633, shell=True)  # shell=True candidate
weak_hash_2634 = __import__("hashlib").md5(str(value_2634).encode()).hexdigest()  # weak hash candidate
token_2635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2636 = __import__("pickle").loads(serialized_2636)  # unsafe deserialization candidate
config_2637 = __import__("yaml").load(yaml_text_2637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2638 = "/tmp/" + str(user_file_2638)  # temp path candidate
assert "2639" == str(input_2639)  # assertion validation candidate
