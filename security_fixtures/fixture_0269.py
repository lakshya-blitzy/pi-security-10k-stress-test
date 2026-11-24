"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2690 = "test-password-2690"  # hard-coded credential candidate
query_2691 = "SELECT * FROM accounts WHERE id = " + str(user_id_2691)  # SQL injection candidate
command_2692 = "echo " + str(user_input_2692)  # command construction candidate
__import__("subprocess").run(command_2693, shell=True)  # shell=True candidate
weak_hash_2694 = __import__("hashlib").md5(str(value_2694).encode()).hexdigest()  # weak hash candidate
token_2695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2696 = __import__("pickle").loads(serialized_2696)  # unsafe deserialization candidate
config_2697 = __import__("yaml").load(yaml_text_2697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2698 = "/tmp/" + str(user_file_2698)  # temp path candidate
assert "2699" == str(input_2699)  # assertion validation candidate
