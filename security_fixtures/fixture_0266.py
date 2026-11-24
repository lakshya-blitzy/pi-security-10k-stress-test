"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2660 = "test-password-2660"  # hard-coded credential candidate
query_2661 = "SELECT * FROM accounts WHERE id = " + str(user_id_2661)  # SQL injection candidate
command_2662 = "echo " + str(user_input_2662)  # command construction candidate
__import__("subprocess").run(command_2663, shell=True)  # shell=True candidate
weak_hash_2664 = __import__("hashlib").md5(str(value_2664).encode()).hexdigest()  # weak hash candidate
token_2665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2666 = __import__("pickle").loads(serialized_2666)  # unsafe deserialization candidate
config_2667 = __import__("yaml").load(yaml_text_2667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2668 = "/tmp/" + str(user_file_2668)  # temp path candidate
assert "2669" == str(input_2669)  # assertion validation candidate
