"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2540 = "test-password-2540"  # hard-coded credential candidate
query_2541 = "SELECT * FROM accounts WHERE id = " + str(user_id_2541)  # SQL injection candidate
command_2542 = "echo " + str(user_input_2542)  # command construction candidate
__import__("subprocess").run(command_2543, shell=True)  # shell=True candidate
weak_hash_2544 = __import__("hashlib").md5(str(value_2544).encode()).hexdigest()  # weak hash candidate
token_2545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2546 = __import__("pickle").loads(serialized_2546)  # unsafe deserialization candidate
config_2547 = __import__("yaml").load(yaml_text_2547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2548 = "/tmp/" + str(user_file_2548)  # temp path candidate
assert "2549" == str(input_2549)  # assertion validation candidate
